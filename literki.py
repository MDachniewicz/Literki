# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:28:33 2022

@author: marek
"""
from random import choice

class literki:
    def words(self):
        filepath = "slowa5.txt"
        f = open(filepath, "r", encoding="utf-8")
        lines= f.readlines()
        words=[]
        for line in lines:
            words.append(line.strip())
        f.close()
        self.words=words   
        
    def words6(self):
        filepath = "slowa6.txt"
        f = open(filepath, "r", encoding="utf-8")
        lines= f.readlines()
        words=[]
        for line in lines:
            words.append(line.strip())
        f.close()
        self.words=words   
        
    def words_top(self):
        filepath = "slowa5_top.txt"
        f = open(filepath, "r", encoding="utf-8")
        lines= f.readlines()
        words=[]
        for line in lines:
            words.append(line.strip())
        f.close()
        self.words_top=words
        
    def words_top6(self):
        filepath = "slowa6_top.txt"
        f = open(filepath, "r", encoding="utf-8")
        lines= f.readlines()
        words=[]
        for line in lines:
            words.append(line.strip())
        f.close()
        self.words_top=words
        
    def random_word(self):
        word = choice(self.words_top)
        while(word not in self.words):
            word = choice(self.words_top)
            
        return word
    
    def __init__(self, num_of_tries=6, word_length=5):
        if word_length==6:
            self.words6()
            self.words_top6()
        else:
            self.words()
            self.words_top()
        self.word_length=word_length
        self.word=self.random_word()
        self.num_of_tries=num_of_tries
        self.win=0
        
    def check_word(self, word):
        return word in self.words
    
    def different_pos(self, character):
        return character in self.word
        
    def guess(self, guess_word):
        feedback=[]
        if(self.check_word(guess_word)==0): print(f'słowa {guess_word} nie ma w slowniku')
        else:
            self.num_of_tries-=1
            if(guess_word==self.word): self.win=1
            for x in range(0, self.word_length):
                if(guess_word[x]==self.word[x]): feedback.append(2)
                elif(self.different_pos(guess_word[x])): feedback.append(1)
                else: feedback.append(0)       
        return feedback
    
    def show_result(self, feedback):
        characters=['-','+','*']
        result=""
        for x in range(0, len(feedback)):
            result+=(characters[feedback[x]])
        print(result)
        
    def play(self):
        while(self.num_of_tries>0 and self.win==0):
            guess=input('Podaj słowo: ')
            feedback=self.guess(guess)
            self.show_result(feedback)
            
        if(self.win==1):print('WYGRAŁEŚ/AŚ !!!')
        else:print(f'PRZEGRAŁEŚ/AŚ !!! \n Chodziło o {self.word}')
        
               
