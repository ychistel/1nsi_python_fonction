Fonction et tableau
===================

Exercice 1:
-----------

#.  On donne la fonction ``sans_effet`` qui prend en paramètre un nombre entier et renvoie son double.

    .. code:: python

        nombre = 13

        def sans_effet(n):
            n = 2*n
            return n

        double = sans_effet(nombre)

    Quelles sont les valeurs des variables ``nombre`` et ``double`` après exécution de ce code ?
    
#.  On donne la fonction ``effet_de_bord`` qui prend en paramètre un tableau de nombres entiers et renvoie un tableau avec les nombres doublés.

    .. code:: python

        tableau = [7,13,20]

        def effet_de_bord(t):
            for i in range(3):
                t[i] = t[i] * 2
            return t

        double = effet_de_bord(tableau)

    Quelles sont les valeurs des variables ``tableau`` et ``double`` ? Que remarquez-vous ?

Exercice 2
-----------

On donne le code en Python suivant:

.. code:: python

    t = [7,9,3,4,8]
    m = t[0]
    for i in range(1,5):
        if t[i] > m:
            m = t[i]

#.  On exécute ce code, quelle est la valeur de la variable ``m`` ?
#.  Transformer ce code en une fonction qui prend en paramètre un tableau de nombres et renvoie la valeur de la variable ``m``.
#.  La fonction ``len`` est une fonction native de Python qui prend en paramètre une variable et renvoie le nombre d'éléments qu'elle contient.

    a.  Dans la console, afficher le nombre d'éléments du tableau de la variable ``t``.
    b.  Modifier votre fonction pour s'adapter aux tableaux qui ont plus de 5 nombres.

#.  Écrire le code de la fonction ``minimum`` qui prend en paramètre un tableau de valeurs et renvoie la plus petite valeur de ce tableau.

Exercice 3
-----------

On donne le code suivant:

.. code:: python

    b = True
    t = [1,2,3,4,5]

    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            b = False

#.  Après exécution de ce code, quelle est la valeur de la variable ``b`` ?
#.  Donner un exemple de tableau pour lequel la variable ``b`` vaut ``False`` après exécution du code.
#.  Écrire ce code avec une fonction qui prend en paramètre un tableau de nombres et renvoie un ``booléen``.
#.  Écrire le code de la fonction ``tri_decroissant`` qui prend en paramètre un tableau de nombres et renvoie ``True`` si le tableau est trié dans l'ordre décroissant et ``False`` s'il ne l'est pas.
#.  La fonction ``est_trie(t,ordre)`` a pour paramètre ``t`` qui est un tableau de nombres et le paramètre ``ordre`` qui indique l'ordre croissant ou décroissant. Cette fonction renvoie ``True`` si le tableau est trié en respectant l'ordre donné et ``False`` dans le cas contraire.

    a.  Quel peut être le type du paramètre ``ordre`` dans la fonction ?
    b.  Écrire le code de la fonction ``est_trie`` et réaliser quelques tests.

Exercice 4
----------

On rappelle que le calcul de la moyenne de plusieurs valeurs consiste à calculer la somme de toutes les valeurs et à la diviser par le nombre total de valeurs.

On rassemble ses valeurs dans un tableau. Par exemple : ``valeurs = [13,17,18]``.

La moyenne de ce tableau est donc : :math:`\dfrac{13+17+18}{3}=\dfrac{48}{3}=16`.

Écrire un code de la fonction ``moyenne`` qui prend en paramètre un tableau de valeurs et renvoie la valeur moyenne. On s'interdit d'utiliser la fonction native ``sum`` pour calculer la somme des valeurs d'un tableau.