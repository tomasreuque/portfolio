{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import PyPDF2\n",
    "import re\n",
    "\n",
    "import spacy\n",
    "from spacy.matcher import Matcher\n",
    "\n",
    "from spacy import displacy\n",
    "NER = spacy.load(\"en_core_web_sm\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import PyPDF2 as pp\n",
    "import re\n",
    "path_pdf = ('/Users/USUARIO/Desktop/python-files/sample.pdf')\n",
    "# Open the PDF file\n",
    "with open(path_pdf, 'rb') as pdf_file:\n",
    "    pdf_reader = pp.PdfReader(pdf_file)\n",
    "    # Get the first page of the PDF\n",
    "    page = pdf_reader.pages[0]\n",
    "    # Extract the text from the page\n",
    "    resume_text = page.extract_text()\n",
    "    #print(resume_text)\n",
    "    # remove linebreaks\n",
    "    new_s = ' '.join(resume_text.splitlines())\n",
    "    # display the string\n",
    "    #print(new_s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mary Murphy      Address      •      Phone      •      email      •      LinkedIn   Tools for Transition Sample Resume   EXECUTIVE ASSISTANT  / PERSONAL ASSISTANT   Providing support to   CFO / CEO / COO / President / Executive Vice President  / Board of Directors    Controller / Director of Human Resources /  Managing Director      Experienced administrative professional with solid background in supporting C -level executives and senior  managers . Uses excellent organizational abilities, clear communication, sense of urgenc y, and willingness to take  on a wide range of responsibilities.     Takes initiative to improve processes in areas such as accounts payable and receivables, human resources ,  recruiting , and general office management . Builds productive and collaborative workin g relationships with  executives,  managers, staff, clients and vendors,  responding to  changing and multiple priorities.  Discrete ,  meticulous, and experienced in working with confidential matters with good judgment .    AREAS OF EXPERTISE    Budget Monitoring   Financial Reporting    Confidential Correspondence   Internal / Offsite Meetings    Domestic / International Travel Arrangements   Multiple Calendar Management    Expense Reports   Personnel Records    Event / Conference Planning   Process Improvements     PROFESSIONAL EXPERIEN CE  Confidentia l……. ………………………. …………………………………………………… …………………… 2007 – 2009      Independent fraud risk management firm                                                                                                               SENIOR ADMINISTRATIVE ASSISTANT   Provid ed support to the Chief Financial Officer, Controller, and Director of Human Resources and Recruiting.   Prepared highly confidential operating and financial information for senior leadership and Board of Directors.    Created and designed various forms and do cuments which bec ame company standard. Designs won  company competition and received special award.    Established new accounts payable entry procedure which improved client  and vendor relations.    Performed key research and made recommendations for managers to purchase and implement new  online recruiting software.     Developed checklist for new hire orientation  which facilitated the process.     Confidential …………………….. …………………………………………………………………………………  2005 – 2007   Leading experiential marketing agency   EXECUTIVE ASSISTAN T  Performed complex administrative duties for the President and Executive Vice President . Produced reports for  budget planning and other management needs.    Oversaw all administrative details for various functions, including internal and offsite meetings.    Collaborated on development and smooth delivery of PowerPoint presentations for monthly meetings to  staff of over 200.     ~  Continued Page 2  ~      \n"
     ]
    }
   ],
   "source": [
    "path_pdf = ('/Users/USUARIO/Desktop/python-files/sample.pdf')\n",
    "pdf_reader = open(path_pdf, 'rb')\n",
    "pdfReader = PyPDF2.PdfReader(pdf_reader)\n",
    "page = pdfReader.pages[0]\n",
    "resume_text = page.extract_text()\n",
    "new_s = ' '.join(resume_text.splitlines())\n",
    "print(new_s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mary Murphy\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "# Define a regular expression pattern for full names\n",
    "name_pattern = re.compile(r'\\b([A-Z][a-z]+\\s[A-Z][a-z]+)\\b')\n",
    "\n",
    "# Extract the first name from the text\n",
    "#text = \"John Smith is a software developer. He works at Google, Jane Doe is a designer and works at Facebook.\"\n",
    "name = name_pattern.search(new_s)\n",
    "\n",
    "# Print the first name\n",
    "print(name.group(1))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)]"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "3282607f385ea6f15702157e2a823b97e47a25ad58852c02230532c044fb265d"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
