def menu(starter, main_course, dessert='Vanila'):
    print(f"""menu is 
    starter = {starter}
    main course = {main_course}
    Dessert = {dessert}""")

def important_for_understanding(arg, result=[]):
    result.append(arg)
    print(result)

important_for_understanding(4)
important_for_understanding(5)
important_for_understanding('hello')

#menu('spring roll','Biryani', 'gulab jamun')
#menu('Biryani', 'gulab jamun','spring roll')

#menu(main_course='Biryani', starter='Spring Roll')
#menu(dessert='Gulab Jamun', main_course='Biryani', starter='Spring roll' )




