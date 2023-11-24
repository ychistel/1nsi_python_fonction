.. 1NSI

.. toctree::
   :maxdepth: 1
   
Activité
========

Le module ``turtle`` propose de nombreuses **fonctions** pour effectuer nos tracés. On rappelle celles qui nous sont utiles :

.. csv-table::
   :header: Fonction Turtle, Rôle de la fonction
   :align: center
   :widths: 30, 70
   :delim: -
   :file: ../csv/instruction_turtle.csv


Les fonctions ``forward`` et ``left`` ont besoin d'une valeur écrite entre parenthèses pour être correctement exécutées par Python. On dit que ces fonctions utilisent un **paramètre**.

.. admonition:: Exemple
   
   .. code-block:: python
   
      left(90)
      forward(100)

D'autres fonctions n'ont pas besoin de valeurs pour être exécutées mais les parenthèses sont quand même présentes ! Les fonctions ``up()`` et ``down()`` qui lève et baisse le crayon sont **sans paramètre**.

Pour finir, une fonction peut avoir besoin de plusieurs valeurs comme la fonction ``goto(x,y)`` où ``x`` et ``y`` sont 2 **paramètres** associés aux coordonnées à atteindre.

Présentation
------------

Certains drapeaux sont constitués de trois rectangles de couleurs différentes. Par exemple, le drapeau français est constitué de 3 rectangles bleu, blanc et rouge. Le drapeau des Pays-Bas est aussi constitué de trois rectangles bleu, blanc et rouge mais disposés horizontalement.

.. image:: ../img/drapeau_fr_pb.svg
   :align: center
   :width: 360px
   
L'objectif est de dessiné ces drapeaux avec le module ``turtle`` en respectant l'odre des couleurs et la disposition verticale ou horizontale des rectangles.

Le script Python sera enregistré dans un fichier ``drapeau.py``. On importera le module ``turtle`` au début du fichier.

1. On prend comme dimensions initales de drapeaux une largeur horizontale de 180 et une hauteur verticale de 120. Définir 2 variables ``L`` et ``H`` définissant la largeur et la hauteur du drapeau à représenter.

2. Pour faire apparaître clairement les drapeaux, on modifie le fond d'écran avec la couleur *lightgray* . Ajouter l'appel de la fonction qui modifie la couleur du fond d'écran et vérifier qu'il s'applique.

3. Le tracé d'un rectangle se réalise avec une boucle ``for``. 
   
   a. Écrire le code pour tracer un rectangle de largeur ``L`` et de hauteur ``H``.
   b. Ajouter les instructions du module ``turtle`` pour mettre en couleur (de votre choix) le rectangle.

Créer des drapeaux avec turtle
------------------------------

Pour créer un drapeau de trois couleurs, il faut tracer 3 rectangles de couleur différente qui s'alignent correctement et dans le bons sens. Cela suppose:

- un positionnement correct du rectangle
- des dimensions pour chaque rectangle
- une disposition verticale ou horizontale
- une couleur pour chaque rectangle

Pour tracer nos drapeaux, nous allons créer nos fonctions. Python permet de créer ses propres fonctions. La syntaxe est la suivante:

.. code-block:: python

   def nom_fonction(paramètre_1,paramètre_2,...):
       instructions à exécuter
       
1. Nous devons déplacer la tortue pour effectuer les tracés. Pendant le déplacement, la tortue n'écrit pas. Une fois arrivée, elle doit pouvoir écrire. 

   Compléter dans votre script, le code de la fonction ``deplacer`` qui prend en paramètre les coordonnées ``x`` et ``y`` à atteindre. On donne la première ligne.

   .. code-block:: python

      def deplacer(x,y):

2. La construction d'un rectangle de couleur est utilisé à plusieurs reprises pour créer un drapeau. L'écriture d'une fonction qui construit ce rectangle s'impose. La fonction ``rectangle`` a 5 paramètres qui sont:

   - ``x`` et ``y`` pour les coordonnées du sommet gauche en bas du rectangle;
   - ``l`` et ``h`` pour la largeur et la hauteur du rectangle;
   - ``couleur`` pour la couleur de remplissage et de tracé du rectangle.

   .. image:: ../img/rectangle.svg
      :align: center
      :width: 360px

   a. Écrire la déclaration de la fonction avec ces 5 paramètres.
   b. Compléter le corps de la fonction en y insérant le code précédent pour tracer un rectangle.
   c. Ajouter le positionnement du sommet bas gauche du rectangle.
   d. Effectuer l'appel ``rectangle(50,0,100,150,"blue") et exécuter le code pour vérifier la construction d'un rectangle bleu``.
   
3. Nous allons écrire le code pour tracer les drapeaux de la Frace et des Pays-Bas qui ont les mêmes couleurs. Nous laisserons une distance de 50 entre chaque drapeau.

   .. image:: ../img/drapeaux_fr_pb.png
      :align: center
      :width: 360px
      
   a. Écrire le code pour créer le drapeau de la France.
   b. Écrire le code pour créer le drapeau des Pays-Bas.
   c. Modifier les valeurs de ``L`` et ``H`` et vérifier que vos drapeaux restent bien tracés. Dans le cas contraire, apporter les modifications nécessaires.
   
   
