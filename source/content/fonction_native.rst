.. 1NSI

.. toctree::
   :maxdepth: 1

Les fonctions en Python
=======================

Comment connaître le nombre de caractères dans une chaine de caratères ?
On peut écrire un script en Python qui permet de connaître ce nombre.
Mais Python dispose déjà de ce script, c’est la **fonction** ``len``.

Par exemple, la chaine de caractères ``"bonjour le monde"`` contient 16
caractères. En Python, pour connaître ce nombre il suffit d’appeler la
fonction avec la chaine de caratères passée en **argument**.

.. admonition:: Exemple

   Dans l’interpréteur python on saisit:

   .. code:: python

      >>> len("bonjour le monde")
      16

Généralités
-----------

Le langage Python dispose de plusieurs fonctions dites **natives** comme
la fonction ``len``. Ces fonctions permettent de réaliser des calculs et
d’agir sur les variables.

Une fonction est définie par un **nom** et par les **paramètres** dont
elle a besoin pour être exécutée. Les paramètres sont placés entre
parenthèses juste après le nom de la fonction.

La syntaxe d’une fonction est donc :
``nom_de_fonction(paramètre_1, paramètre_2,...)``.

Une fonction :

-  peut avoir 0, 1, 2, plusieurs paramètres.
-  peut avoir des paramètres **optionnels** qui ont une valeur par
   défaut; il est possible de modifier cette valeur à l’appel de la
   fonction en précisant entre parenthèses
   ``paramètre = nouvelle valeur``.
-  respecte l’ordre des paramètres.

On appelle **arguments** les valeurs fournies à la fonction lors de l'appel.
Chaque argument sera affecté, dans l'ordre, à chaque paramètre de la fonction.

Quelques fonctions utiles
-------------------------

Les fonctions natives sont répertoriées sur le site de la `documentation
Python <https://docs.python.org/fr/3/library/functions.html>`__.

On donne un bref aperçu de quelques unes de ce fonctions à travers des
usages qui nous seront utiles cette année.

**abs(x)**

La fonction mathématique ``abs`` prend en argument un nombre et renvoie
sa valeur absolue, c’est à dire transformé en nombre positif.

.. admonition:: Exemple

   >>> a = 3.5
   >>> b = -2
   >>> c = abs(a)
   >>> d = abs(b)
   >>> print(c,d)
   3.5 2
    
   les variables `c` et `d` ont pour valeurs respectives `3.5` et `2`

**float(x)**

La fonction ``float`` prend en argument un nombre ou une chaine de
caractères numériques et renvoie un nombre à virgule, un flottant.

.. admonition:: Exemple

   >>> a = float(5)
   >>> b = float('1E03')
   >>> c = float('-4.6')
   
   les variables `a`, `b` et `c` ont pour valeurs respectives `5.0`, `1000.0` et `-4.6`

**help(objet)**

La fonction ``help`` prend en argument un objet Python qui peut être une
fonction ou une variable et renvoie l’aide native sur celui-ci.

Si la fonction est exécutée sans argument ``help()``, un programme
d’aide démarre dans l’interpréteur.

.. admonition:: Exemple

   >>> help(abs)
   
   L'aide sur la fonction `abs` est affichée:
    
      Help on built-in function abs in module builtins:

      abs(x, /)
         Return the absolute value of the argument.

**input(prompt)**

La fonction input permet de saisir une valeur par un utilisateur. Le
``prompt`` est affiché et peut constituer un guide pour la saise. La
valeur saisie sera convertie en chaine de caractères.

.. admonition:: Exemple

   >>> input("Comment allez-vous ? ")
   Comment allez-vous ? bien
   'bien'
   
   Dans l'interpréteur, une ligne de saisie est proposée avec le message "Comment allez-vous ?"
   Après la saisie de la valeur, celle-ci est affichée.

**int(x,base=10)**

La fonction ``int`` transforme en nombre entier l’argument passé en
paramètre. On peut remarquer la présence d’un paramètre optionnel
``base`` qui a pour valeur 10 par défaut.

Si la valeur passée en argument est un flottant, alors la fonction
renvoie la partie entière du flottant, c’est à dire la partie avent la
virgule.

.. admonition:: Exemple

   >>> a = int(-4.1)
   >>> b = int(3.5)
   >>> c = int('1E3')
    
   les variables `a`, `b` et `c` ont pour valeurs respectives `-5`, `3` et `1000`.

**len(x)**

La fonction ``len`` renvoie le nombre d’éléments contenus dans la
variable ``x``. Cette fonction s’applique sur des variables de type
**string** et **list** qui ont plusieurs éléments.

.. admonition:: Exemple

   >>> a = len("bonjour")
   >>> b = len([4,5,6])
    
   la variable `a` a pour valeur `7` puisque le mot *bonjour* a 7 lettres.
   la variable `b` a pour valeur `3` puisque la liste contient 3 nombres.

**pow(base,exp)**

La fonction mathématique ``pow`` calcule une puissance du nombre passé
en argument du paramètre ``base`` élevé à la puissance ``exp``.

Cette fonction est finalement équivalente à ``base**exp``.

.. admonition:: Exemple

   >>> a = pow(4,2)
   >>> b = pow(2,-1)
    
   les variables `a` et `b` ont pour valeurs respectives :math:`4^2=16` et :math:`2^{-1}=0.5`.

**print(variables, sep=’ ‘, end=’:raw-latex:`\n`’)**

Cette fonction permet d’afficher un message, une valeur ou la
combinaison des deux. Elle prend en paramètre une chaine de caractères
et/ou une variable. Elle s’applique aux variables quel que soit leur
type.

La fonction possède des paramètres optionnels:

- le paramètre ``sep=' '`` qui est le séparateur affiché entre les valeurs
- le paramètre ``end='\n'`` qui réalise un retour à la ligne pour l’affichage suivant.

.. admonition:: Exemple

   1. Afficher un message:
    
      >>> print("Bonjour")
    
   2. Afficher la valeur d'une variable:
    
      >>> a = 5
      >>> print(a)
    
   3. Afficher une variable accompagnée d'un message:
    
      >>> a = 5
      >>> print("La valeur de a est:",a)
    
   4. Changer de séparateur entre plusieurs variables:
    
      >>> a,b,c = 4,5,6
      >>> print(a,b,c,end="<")
    
      L'affichage en console sera : `4 < 5 < 6`

**round(n,ndigits)**

La fontion ``round`` renvoie le nombre ``n`` arrondi avec une précision
de ``ndigits`` chiffres après la virgule. Si ``ndigits`` est omis (ou
est None), l’entier le plus proche est renvoyé.

.. admonition:: Exemple

    >>> a = round(4.63)
    >>> b = round(4.63,1)
    
    les variables `a` et `b` ont pour valeurs respectives `5` et `4.6`.

**type(variable)**

La fontion ``type`` renvoie le type de la variable passée en paramètre.

.. admonition:: Exemple

    >>> a = 4
    >>> b = 4.63
    >>> type(a)
    <class 'int'>
    >>> type(b)
    <class 'float'>
    
    la variable `a` est de type `int` et la variable `b` est de type `float`.
