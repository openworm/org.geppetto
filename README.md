<p align="center">
  <img src="https://raw.githubusercontent.com/tarelli/bucket/master/geppetto%20logo.png" alt="Geppetto logo"/>
</p>

# [Geppetto](http://www.geppetto.org/)
<img width="1184" alt="geppetto_in_overview" src="https://user-images.githubusercontent.com/1573896/44878488-ffa53100-ac74-11e8-9280-e7d579a7accd.png">

[![Stories in Ready](https://badge.waffle.io/openworm/org.geppetto.png?label=ready&title=Ready)](https://waffle.io/openworm/org.geppetto)
[![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](http://stackshare.io/tarelli/geppetto)

#### [Website](http://www.geppetto.org/) | [Documentation](http://docs.geppetto.org/) | [Releases](https://github.com/openworm/org.geppetto/releases/)
#### [Contribution guidelines](http://docs.geppetto.org/en/latest/contribute.html#how-to-contribute-code-to-geppetto) | [Development progress](https://waffle.io/openworm/org.geppetto)

**Geppetto is an open-source platform to build web-based applications to visualize and simulate neuroscience data and models.**

**If you just want to play with a demo Geppetto deployment you don't need to install anything, just visit <https://live.geppetto.org>.**

If you want to setup your own Geppetto deployment from sources use our [Setup Instructions](http://docs.geppetto.org/en/latest/osxlinuxsetup.html). If you need help building a neuroscience application using Geppetto or if you want to join the project as a contributor you can [send an email](mailto:matteo@geppetto.org) or just interact with us through GitHub!

This is the umbrella project that keeps together all the different Geppetto modules currently available:

#### Java backend
The Java backend is used in client-server deployments of Geppetto. The Java backend is modular allowing each deployment to be customised only with the relevant bundles.
 * Essential
   * [org.geppetto.model](https://github.com/openworm/org.geppetto.model) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model)
   * [org.geppetto.core](https://github.com/openworm/org.geppetto.core) [![Build Status](https://travis-ci.org/openworm/org.geppetto.core.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.core)
   * [org.geppetto.simulation](https://github.com/openworm/org.geppetto.simulation) [![Build Status](https://travis-ci.org/openworm/org.geppetto.simulation.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.simulation)
   * [org.geppetto.frontend](https://github.com/openworm/org.geppetto.frontend) [![Build Status](https://travis-ci.org/openworm/org.geppetto.frontend.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.frontend) (Note: The frontend is resused on all backends)
 * Optional
    * [org.geppetto.persistence](https://github.com/openworm/org.geppetto.persistence) [![Build Status](https://travis-ci.org/openworm/org.geppetto.persistence.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.persistence)
    * [org.geppetto.datasources](https://github.com/openworm/org.geppetto.datasources) [![Build Status](https://travis-ci.org/openworm/org.geppetto.datasources.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.datasources)
 * Domain Specific
    * Neuroscience
       * [org.geppetto.model.neuroml](https://github.com/openworm/org.geppetto.model.neuroml) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.neuroml.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model.neuroml)
       * [org.geppetto.simulator.external](https://github.com/openworm/org.geppetto.simulator.external) [![Build Status](https://travis-ci.org/openworm/org.geppetto.simulator.external.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.simulator.external)
       * [org.geppetto.model.swc](https://github.com/openworm/org.geppetto.model.swc) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.swc.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model.swc)
       * [org.geppetto.model.nwb](https://github.com/openworm/org.geppetto.model.nwb) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.nwb.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model.nwb)
     * Fluid mechanics (Currently in development)
        * [org.geppetto.sibernetic](https://github.com/openworm/org.geppetto.sibernetic) [![Build Status](https://travis-ci.org/openworm/org.geppetto.sibernetic.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.sibernetic)

#### Python Backend (prototype, in development)
The Python backend is based on a Geppetto Jupyter extension which allows the user to interact with the Geppetto frontend from Python. This deployment makes it ideal to use Geppetto as a visualization/computational local playground.
   * [org.geppetto.frontend.jupyter](https://github.com/openworm/org.geppetto.frontend.jupyter) [![Build Status](https://travis-ci.org/openworm/org.geppetto.frontend.jupyter.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.frontend.jupyter)
   * [pyGeppetto](https://github.com/openworm/pygeppetto)

#### Node.js Backend (proof of concept)
   * [org.geppetto.frontend.nodejs](https://github.com/openworm/org.geppetto.frontend.nodejs) [![Build Status](https://travis-ci.org/openworm/org.geppetto.frontend.nodejs.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.frontend.nodejs)


Geppetto is an open-source project with a growing community, if you want to contribute (with either new simulators support, visualisation widgets or backend magic) please do get in touch at <info@geppetto.org> or fork any of the bundles and do what you please.


#### [Website](http://www.geppetto.org/) | [Documentation](http://docs.geppetto.org/) | [Releases](https://github.com/openworm/org.geppetto/releases/)
#### [Contribution guidelines](http://docs.geppetto.org/en/latest/contribute.html#how-to-contribute-code-to-geppetto) | [Development progress](https://waffle.io/openworm/org.geppetto)

Geppetto is released under the [MIT](http://opensource.org/licenses/MIT) license.

<p align="center">
  <img src="http://www.geppetto.org/images/geppetto.png" alt="Geppetto"/>
</p>
