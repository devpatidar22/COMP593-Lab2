def main():
    dic_Name = {'full_name': "Bob Loblaw",
                'student_id': 123456789,
                'pizza_toppings': ["PINEAPPLE", "SAUSAGE", "PEPPERONI"],
                'movies': [{'title': 'dune', 'genre': 'sci-fi'}, {'title': 'the hangover', 'genre': 'comedy'}]
                }

    newMovie = {'title': 'the lord Of the rings', 'genre': 'fantasy'}
    dic_Name['movies'].append(newMovie)

    newPizzaTopping = ('BACON', 'HOT PEPPERS')

    s_name(dic_Name)
    print()
    print_pizza(dic_Name)
    print()
    add_pizza(dic_Name, newPizzaTopping)
    print_pizza(dic_Name)
    print()
    list_movie_genre(dic_Name)
    print()
    new_list(dic_Name['movies'])
    return dic_Name


def s_name(ds):
    full_name = ds['full_name']
    first_name = full_name.split(" ")[0]
    student_id = ds['student_id']
    print(f"My name is {full_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.")
    return


def add_pizza(ds, tuple):
    ds['pizza_toppings'] += tuple
    ds['pizza_toppings'].sort()
    for i in range(len(ds['pizza_toppings'])):
        ds['pizza_toppings'][i] = ds['pizza_toppings'][i].lower()


def print_pizza(ds):
    print('My favourite pizza toppings are:')
    for i in range(len(ds["pizza_toppings"])):
        items = ds['pizza_toppings'][i]
        print(f'-{items}')


def list_movie_genre(ds):
    print('I like to watch ', end='')
    for i in range(len(ds['movies'])):
        if i + 1 < len(ds['movies']):
            print(ds['movies'][i]['genre'], end=', ')
        elif i + 1 == len(ds['movies']):
            print(f"and {ds['movies'][i]['genre']}", end=' ')
    print("movies.")


def new_list(ml):
    print("Some of my favourite movies are", end=' ')
    for i in range(len(ml)):
        if i + 1 < len(ml):
            x = ml[i]['title'].split(' ')
            for i in range(len(x)):
                x[i] = x[i].capitalize()
            print(' '.join(x), end=', ')
        elif i + 1 == len(ml):
            y = ml[i]['title'].split(' ')
            for i in range(len(y)):
               y[i] = y[i].capitalize()
            print(f"and {' '.join(y)}", end='')

    print('!')


if __name__ == '__main__':
    main()