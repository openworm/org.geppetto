[![Stories in Ready](https://badge.waffle.io/openworm/org.geppetto.png?label=ready&title=Ready)](https://waffle.io/openworm/org.geppetto)
<p align="center">
  <img src="https://dl.dropboxusercontent.com/u/7538688/geppetto%20logo.png?dl=1" alt="Geppetto logo"/>
</p>

# [Geppetto](http://www.geppetto.org/)

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/openworm/org.geppetto?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

#### [Website](http://www.geppetto.org/) | [Documentation](http://docs.geppetto.org/) | [Install Instructions](http://docs.geppetto.org/en/latest/install.html) | [Releases](https://github.com/openworm/org.geppetto/releases/)
#### [Contribution guidelines](http://docs.geppetto.org/en/latest/contribute.html#how-to-contribute-code-to-geppetto) | [Development progress](https://waffle.io/openworm/org.geppetto)


Geppetto is a web-based multi-algorithm, multi-scale simulation platform engineered to support the simulation of complex biological systems and their surrounding environment. 

Although Geppetto was designed with systems biology in mind, thanks to its generic architecture Geppetto can be used anywhere there is need to rely on a backend to perform any kind of simulation which then needs to be streamed to a web client, allowing the user to interact with the simulation remotely and through an API (accessible from an embedded Javascript console) and a set of customisable widget which allows visualising data in different ways.

Geppetto is a modular platform based on Java, OSGi and Spring and different modules (also named bundles) provide different functionalities.

This is the umbrella project that keeps together all the different modules currently available:
 * Essential
   * [org.geppetto.model](https://github.com/openworm/org.geppetto.model) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model)
   * [org.geppetto.core](https://github.com/openworm/org.geppetto.core) [![Build Status](https://travis-ci.org/openworm/org.geppetto.core.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.core)
   * [org.geppetto.simulation](https://github.com/openworm/org.geppetto.simulation) [![Build Status](https://travis-ci.org/openworm/org.geppetto.simulation.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.simulation)
   * [org.geppetto.frontend](https://github.com/openworm/org.geppetto.frontend) [![Build Status](https://travis-ci.org/openworm/org.geppetto.frontend.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.frontend)
 * Optional
    * [org.geppetto.persistence](https://github.com/openworm/org.geppetto.persistence) [![Build Status](https://travis-ci.org/openworm/org.geppetto.persistence.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.persistence)
 * Domain Specific
   * Neuronal domain
     * [org.geppetto.model.neuroml](https://github.com/openworm/org.geppetto.model.neuroml) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.neuroml.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model.neuroml)
     * [org.geppetto.simulator.external](https://github.com/openworm/org.geppetto.simulator.external) [![Build Status](https://travis-ci.org/openworm/org.geppetto.simulator.external.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.simulator.external)
     * [org.geppetto.model.swc](https://github.com/openworm/org.geppetto.model.swc) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.swc.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model.swc)
 * Previous releases
    * Neuronal domain
     * [org.geppetto.simulator.jlems](https://github.com/openworm/org.geppetto.simulator.jlems) [![Build Status](https://travis-ci.org/openworm/org.geppetto.simulator.jlems.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.simulator.jlems)
   * Fluid mechanics  (Release 0.2.7)
      * [org.geppetto.model.sph](https://github.com/openworm/org.geppetto.model.sph) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.sph.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model.sph)
     * [org.geppetto.solver.sph](https://github.com/openworm/org.geppetto.solver.sph) [![Build Status](https://travis-ci.org/openworm/org.geppetto.solver.sph.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.solver.sph)
     * [org.geppetto.simulator.sph](https://github.com/openworm/org.geppetto.simulator.sph) [![Build Status](https://travis-ci.org/openworm/org.geppetto.simulator.sph.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.simulator.sph)

  
Geppetto is an open-source project with a growing community, if you want to contribute (with either new simulators support, visualisation widgets or backend magic) please do get in touch at <info@geppetto.org> or fork any of the bundles and do what you please.


#### [Website](http://www.geppetto.org/) | [Documentation](http://docs.geppetto.org/) | [Install Instructions](http://docs.geppetto.org/en/latest/install.html) | [Releases](https://github.com/openworm/org.geppetto/releases/)
#### [Contribution guidelines](http://docs.geppetto.org/en/latest/contribute.html#how-to-contribute-code-to-geppetto) | [Development progress](https://waffle.io/openworm/org.geppetto)

Geppetto is released under the [MIT](http://opensource.org/licenses/MIT) license.

