.. 1NSI

.. toctree::
   :maxdepth: 1

Créer ses fonctions
===================

Lorsqu’un programme contient des blocs de code **semblables** utilisés à
plusieurs reprises, il est plus efficace d’écrire ce bloc de code
dans une **fonction** et de remplacer chaque bloc du programme par un
**appel** à la fonction.

Cela donne une structure différente au programme. On écrit en premier
toutes les fonctions puis le programme principal contenant les appels
aux différentes fonctions.

.. image:: ../img/fonction_1.svg
    :align: center
    :width: 300px
    :alt: image svg

On trouve plusieurs avantages à créer ses fonctions:

-  la maintenance du code est plus facile; il suffit de modifier la
   fonction ce qui évite de modifier tous les blocs de code éparpillés
   dans le programme principal.
-  une fonction est réutilisable plusieurs fois
-  le programme principal est rendu plus lisible
-  une fonction peut utiliser des paramètres qui font référence aux
   variables du programme

.. admonition:: Attention

   - Les variables du programme principal sont **globales** et accessibles n'importe où dans le programme.
   - Les variables d'une fonction sont **locales** et donc **uniquement** accessible dans la fonction.

En Python
---------

La syntaxe pour créer une fonction est la suivante : ``def <nom_fonction>([paramètres]):``

Expliquons les différentes parties de cette syntaxe:

-  ``def`` est le mot clef qui informe Python qu’une fonction est créée;
-  ``<nom_fonction>`` est le nom qui identifie la fonction;
-  ``[paramètres]`` représentent les différents paramètres utilisés par
   la fonction pour renvoyer une valeur. Il peut y avoir aucun ou 1 ou 2
   ou plusieurs paramètres. Ces paramètres sont remplacés par des
   valeurs lorsque la fonction est appelée dans le programme principal;
-  Les deux points ``:`` termine la définition de la fonction et
   provoque une indentation des instructions contenues dans la fonction.
- L'instruction ``return`` met fin à l'exécution de la fonction qui renvoie la valeur située juste après le mot clé ``return``.

.. admonition:: Exemple

	.. literalinclude:: ../python/cours.py
		:lines: 1-
	
	Dans l'interpréteur, on **appelle la fonction** avec deux arguments numériques:
	
	>>> ma_fonction(2,3)
	5
   
   - La fonction calcule la valeur ``a+b`` soit :math:`2+3` et l'affecte à la variable locale ``x``.
   - La fonction renvoie la valeur contenue dans la variable ``x``.
   
