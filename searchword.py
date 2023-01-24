{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5hCZD9fZX1wunQ0wHnQ8t",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/veesesh/pythonlab/blob/main/searchword.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1lYgbB3wL7eH",
        "outputId": "684229ab-61f2-43f4-9d54-8cb74d33e8c8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a word you want to search in file: meow\n",
            "word found\n"
          ]
        }
      ],
      "source": [
        "with open('search.txt') as file:\n",
        "    contents = file.read()\n",
        "    search_word = input(\"enter a word you want to search in file: \")\n",
        "    if search_word in contents:\n",
        "        print ('word found')\n",
        "    else:\n",
        "        print ('word not found')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "NDfSlxSkNnHJ"
      }
    }
  ]
}