# IQSIRON
Character detection with OCR -Python-

## Required Packages
pyocr (Required)
```py
!pip install pyocr
```

## Optional Packages
1. libheif (Option: for HEIC images)
```py
!apt install libheif-examples
```

2. googletrans (Option: Translate the result)
```py
!pip install googletrans
```

## Usage
1. If you want use HEIC pictures, you need to convert to jpg. (Recommend libheif)

2. Detect character with OCR. That code is included in main.py 

   And the result is defined by "text".
   
Option1: You can translate the result with Google Translation. That code is included in translate.py.

Option2: You can check the degree of similarity between the result and text file that you prepared. That code is included in similarity.py

## Google Colaboratory

**Japanese**:
https://colab.research.google.com/drive/1pD-b78DiisueMHf-83yyytGxSNUyMZQx?usp=sharing

**English**:
https://colab.research.google.com/drive/1p1hpmzgDXNG6wqf9QRP9skOibAbs6b0a?usp=sharing


## LICENSE
This software is released under the GNU General Public License.


