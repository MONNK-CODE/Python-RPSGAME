{
 "cells": [
  {
   "metadata": {},
   "cell_type": "code",
   "outputs": [],
   "execution_count": null,
   "source": [
    "import random as r\n",
    "materials = [\"Rock\", \"Paper\", \"Scissors\"]\n",
    "computer_choice = r.choice(materials)\n",
    "restart = 'yes'\n",
    "while(restart == 'yes'):\n",
    "    user_choice = input(\"Choose Rock, Paper, or Scissors: \")\n",
    "    if user_choice in materials:\n",
    "        print(\"You chose: \", user_choice)\n",
    "        print(\"Computer chose: \", computer_choice)\n",
    "\n",
    "    if user_choice == computer_choice:\n",
    "        print(\"It's a tie!\")\n",
    "\n",
    "    elif user_choice == \"Rock\" and computer_choice == \"Scissors\":\n",
    "        print(\"You win!\")\n",
    "    elif user_choice == \"Paper\" and computer_choice == \"Rock\":\n",
    "        print(\"You win!\")\n",
    "    elif user_choice == \"Scissors\" and computer_choice == \"Paper\":\n",
    "        print(\"You win!\")\n",
    "\n",
    "\n",
    "    elif  computer_choice == \"Rock\" and user_choice == \"Scissors\":\n",
    "        print(\"Computer Wins!\")\n",
    "    elif  computer_choice == \"Paper\" and user_choice == \"Rock\":\n",
    "        print(\"Computer Wins!\")\n",
    "    elif  computer_choice == \"Scissors\" and user_choice == \"Paper\":\n",
    "        print(\"Computer Wins!\")\n",
    "    else: \n",
    "        print(\"Invalid choice. Please choose Rock, Paper, or Scissors.\") \n",
    "    restart = input('Do you want to play again?(yes or no) ')  "
   ],
   "id": "40858f3fd17828a"
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
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
