#!/bin/bash

for palavra in $( cat word_list.txt ); do

host $palavra.www.site.com

done



#Word list vai conter a .pop .email .admin. smtp. 
