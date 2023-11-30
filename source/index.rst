Les fonctions en Python
=======================

Nous avons utilisé le module ``turtle`` pour réaliser des dessins. Ce module propose de nombreuses **fonctions** pour effectuer nos tracés. On en rappelle quelques-unes:

.. csv-table::
   :header: Fonction Turtle, Action
   :align: center
   :widths: 30, 70
   :delim: -
   :file: csv/fonction_turtle.csv

Les fonctions ``forward`` et ``left`` ont besoin d'un nombre écrit entre les parenthèses pour être correctement exécutées par Python. On dit que ces fonctions utilisent un **paramètre**.

.. admonition:: Exemple
   
   .. code-block:: python
   
      left(90)
      forward(100)

D'autres fonctions n'ont pas besoin de valeurs pour être exécutées mais les parenthèses sont quand même présentes ! Les fonctions ``up()`` et ``down()`` qui lève et baisse le crayon sont **sans paramètre**.

Pour finir, une fonction peut avoir besoin de plusieurs valeurs comme la fonction ``goto(x,y)`` où ``x`` et ``y`` sont 2 **paramètres** associés aux coordonnées à atteindre.

.. warning::

   Une **fonction** se note toujours avec des parenthèses situées juste après son nom.

Comme le module ``Turtle``, nous pouvons créer nos propres fonctions en respectant une syntaxe imposée par le langage Python. La création de fonction apporte de nombreux avantages à un programme:

- une fonction permet de centraliser des blocs d'instructions qui se répètent plusieurs fois dans un programme;
- une fonction est plus facile à debugger qu'un bloc d'instructions noyé dans un programme;
- une fonction peut être appelée autant de fois que nécessaire;
- une fonction peut renvoyer une ou plusieurs valeurs utilisées par le programme.


.. toctree::
   :maxdepth: 1
   :hidden:
   
   content/activite.rst
   content/fonction.rst
   content/exercice.rst  
   content/exercice_approfondissement.rst
