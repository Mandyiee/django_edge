import os, bs4
from pathlib import Path

#start from scratch dir

#/home/mandyiee/Documents/python/django/test-folder
#/home/mandyiee/Documents/python/django/core
def django_edge():
    try:

        filled = False

        while filled == False:

            print('Input the file path to your templates folder')

            templateInput = input()

            templateDir = Path(templateInput)

            print('Input the file path your core folder')

            coreInput = input()

            coreDir = Path(coreInput)
            
            if templateInput != '' and coreInput != '':
                if os.path.exists(templateDir) and os.path.exists(coreDir):
                    if os.path.isdir(templateDir) and os.path.isdir(coreDir):
                        filled = True
                    else:
                        print('your file path is not a folder')
                        print('')
                else:
                    print('your file path does not exist')
                    print('')
            else:
                print('Invalid Input. Please Try Again')
                print('')
                

        os.chdir(Path.home())
        os.chdir(Path(templateDir))

        filenames = []

        file_names = []

        workingFolder = Path.cwd()

        print('what folder path should be removed eg. assets/. Leave blank if you have nothing.')
        removedFolder = input()

        for file in workingFolder.glob('*.html'):
            filename = os.path.basename(file)
            
            #without extension
            file_name = os.path.splitext(filename)
            filenames.append(filename)

            file_names.append(file_name)

            htmlFile = open(filename,'r',encoding='utf8')
            soup = bs4.BeautifulSoup(htmlFile.read(), 'html.parser')  
            images = soup.select('img')
            for image in images:
                firstSrc = image.get('src')
                if firstSrc:
                    if 'static' not in firstSrc:
                        if 'http' not in firstSrc:
                            firstSrc = firstSrc.replace(removedFolder,'')
                            secondSrc = "{% static '" + firstSrc +"' %}"
                            image['src'] = secondSrc
                else:
                    continue
            links = soup.select('link')
            for link in links:
                firstSrc = link.get('href')
                if firstSrc:
                    if 'static' not in firstSrc:
                        if 'http' not in firstSrc:
                            firstSrc = firstSrc.replace(removedFolder,'')
                            secondSrc = "{% static '" + firstSrc +"' %}"
                            link['href'] = secondSrc
                else:
                    continue
            scripts = soup.select('script')
            for script in scripts:
                firstSrc = script.get('src')
                if firstSrc:
                    if 'static' not in firstSrc:
                        if 'http' not in firstSrc:
                            firstSrc = firstSrc.replace(removedFolder,'')
                            secondSrc = "{% static '" + firstSrc +"' %}"
                            script['src'] = secondSrc
                else:
                    continue
            alinks = soup.select('a')
            for alink in alinks:
                firstSrc = alink.get('href')
                if firstSrc:
                    if '.html' in firstSrc:
                        firstSrc = firstSrc.replace('.html','')
                        firstSrc = firstSrc.replace(removedFolder,'')
                        secondSrc = "/" + firstSrc
                        alink['href'] = secondSrc
                else:
                    continue
                
            with open(filename, "wb") as f_output:
                loads = '{% load static %}'
                loads_byte = loads.encode('utf-8')
                f_output.write(loads_byte)
                f_output.write(soup.prettify("utf-8"))
                print('done')
                print('')
            print('done with this ' + filename)
            print('')


        os.chdir(Path.home())   
        os.chdir(Path(coreDir))
        with open("views.py", "r") as f:
            checkFile = f.read()
            if 'views created' in checkFile:
                print('views already created')
                print('')
            else:
                with open("views.py", "a") as f:
                    for i in range(len(filenames)):
                        text = f"""
        def {file_names[i][0].replace('-','_')}(request):
            return render(request,'{file_names[i][0]}.html')
                        """
                        f.write(text)
                    f.write("#views created")
                    
                    
                    
        if os.path.exists('urls.py'):
            with open("urls.py", "r") as f:
                checkFile = f.read()
                if 'urls created' in checkFile:
                    print('urls already created')
                else:
                    with open("urls.py", "w") as f:
                        f.write("""from django.urls import path
from . import views

urlpatterns = [                   
                                """)
                        for i in range(len(filenames)):
                            if filenames[i] == 'index.html':
                                text = f"""path('',views.{file_names[i][0]}, name='{file_names[i][0]}'),
                                """
                                f.write(text)
                                continue

                            text = f"""path('{file_names[i][0]}',views.{file_names[i][0].replace('-','_')}, name='{file_names[i][0]}'),
                            """
                            f.write(text)
                        
                        f.write("""
            ]
            #urls created                   
                                """)  
        else:
            with open("urls.py", "w") as f:
                        f.write("""from django.urls import path
from . import views


urlpatterns = [                   
                                """)
                        for i in range(len(filenames)):
                            if filenames[i] == 'index.html':
                                text = f"""path('',views.{file_names[i][0]}, name='{file_names[i][0]}'),
                                """
                                f.write(text)
                                continue

                            text = f"""path('{file_names[i][0].replace('-','_')}',views.{file_names[i][0].replace('-','_')}, name='{file_names[i][0].replace('-','_')}'),
                            """
                            f.write(text)
                        
                        f.write("""
            ]
            #urls created                   
                                """)  

    
        
    except Exception as e:
        print('An error occurred')
        print(e)