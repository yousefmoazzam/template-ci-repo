Introduction
=============

Description of project.

Section 1
------------

Text regarding section 1

Subsection 1-1
~~~~~~~~~~~~~~~~~

Text regarding subsection 1-1

Section 2 - Some examples
-------------------------

Hyperlinking
~~~~~~~~~~~~

A `hyperlink`_ whose destination is specified at the end of the source file.

Boxed text
~~~~~~~~~~

.. note::

    Text in a box.

Bullet pointed list
~~~~~~~~~~~~~~~~~~~

- Item A
- Item B
- Item C

Numbered list
~~~~~~~~~~~~~

#. Item A
#. Item B
#. Item C

Table
~~~~~

.. list-table:: Table Title
    :widths: 50, 50
    :header-rows: 1

    * - Header 1
      - Header 2
    * - Entry 1-1
      - Entry 2-1
    * - Entry 1-2
      - Entry 2-2

Diagrams
~~~~~~~~

Sphinx is able to create many different types of diagrams and graphs using
Graphviz. Below are two examples, but a good resource for more in-depth
information is available `here`_.

Simple diagram
~~~~~~~~~~~~~~

.. digraph::  small_diagram

    bgcolor=transparent
    node [fontname=Arial fontsize=10 shape=box style=filled fillcolor="#8BC4E9"]
    edge [fontname=Arial fontsize=10 arrowhead=vee]

    Intermediate [label="[Record(),\n Widget(),\n AsynParam(), \nTemplateInclude()]"]
    Products [label="Template\nScreens\nDriver Params\nDocumentation"]

    {rank=same; Components -> Intermediate -> Producer -> Products}
    Defines -> Components
    Takes -> Producer

More complicated diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. digraph:: bigger_diagram

    bgcolor=transparent
    rankdir=LR
    node [fontname=Arial fontsize=10 shape=box style=filled fillcolor="#8BC4E9"]
    edge [fontname=Arial fontsize=10 arrowhead=vee]

    {   rank=same;
        "pilatus.yaml"
        "pilatus_logic.template"
        "pilatus.cpp"
        "pilatus.h"
    }

    PVI [shape=doublecircle]
    "pilatus.yaml" -> PVI
    PVI -> "pilatus_parameters.cpp"
    PVI -> "pilatus_parameters.h"
    PVI -> "pilatus.template"
    PVI -> "pilatus_parameters.opi"
    PVI -> "pilatus_parameters.adl"
    PVI -> "pilatus_parameters.edl"
    PVI -> "pilatus_docs.html"
    "pilatus_logic.template" -> "pilatus.template" [label="include"]
    "pilatus_parameters.cpp" -> "libPilatus.so"
    "pilatus_parameters.h" -> "libPilatus.so"
    "pilatus.cpp" -> "libPilatus.so"
    "pilatus.h" -> "libPilatus.so"

Code block
~~~~~~~~~~

.. code-block:: cpp

    #ifndef PILATUS_PARAMETERS_H
    #define PILATUS_PARAMETERS_H

    /* Strings defining the parameter interface with the Database */
    #define ThresholdEnergyString "THRESHOLDENERGY" /* (asynFloat64, r/w) */

    /* Class definition */
    class PilatusParameters {
    public:
        PilatusParameters(asynPortDriver *parent);
        /* Parameters */
        int ThresholdEnergy;
    }

    #endif //PILATUS_PARAMETERS_H

Code diff
~~~~~~~~~

.. code-block:: diff

     pilatusDetector::pilatusDetector(const char *portName, ...)
         : ADDriver(portName, ...), ...
    -    imagesRemaining(0)
    +    imagesRemaining(0),
    +    PilatusParameters(this)
     {
    -    createParam(ThresholdEnergyString, asynParamFloat64, &ThresholdEnergy);
         status = (epicsThreadCreate("PilatusDetTask", ...

.. _hyperlink:
    https://readthedocs.org

.. _here:
    https://build-me-the-docs-please.readthedocs.io/en/latest/Using_Sphinx/UsingGraphicsAndDiagramsInSphinx.html
