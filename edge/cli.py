"""
The command-line interface for the downloader
"""
import argparse
from .django import django_edge



def main():
    parser = argparse.ArgumentParser(
        description="A package that helps you setup django so that you can focus on the important things."
    )
    # parser.add_argument(
    #     "start", type=str,
    #     help="Start your the django edge pakage"
    # )
    # args = parser.parse_args()
    
    parser.parse_args()
    django_edge()
    print("You can now move on to more important things")

if __name__ == "__main__":
    main()