{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import whisper\n",
    "\n",
    "model = whisper.load_model('small', device='cuda')\n",
    "result = model.transcribe('audio1.wav')\n",
    "result"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "hololens2",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
