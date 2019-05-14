<p align="center">
  <img src="https://raw.githubusercontent.com/tarelli/bucket/master/geppetto%20logo.png" alt="Geppetto logo"/>
</p>

# [Geppetto](http://www.geppetto.org/)

[![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](http://stackshare.io/tarelli/geppetto)

#### [Website](http://www.geppetto.org/) | [Documentation](http://docs.geppetto.org/) | [Releases](https://github.com/openworm/org.geppetto/releases/)
#### [Contribution guidelines](http://docs.geppetto.org/en/latest/contribute.html#how-to-contribute-code-to-geppetto) | [Development progress](https://waffle.io/openworm/org.geppetto)

**Geppetto is an open-source platform to build web-based applications to visualize and simulate neuroscience data and models.**

**If you want to play with a demo application built with Geppetto just visit <https://live.geppetto.org>.**

If you want to build your own Geppetto application follow these [instructions](http://docs.geppetto.org/en/latest/build.html) and [these steps](http://docs.geppetto.org/en/latest/osxlinuxsetup.html) to setup the source code using the Java Backend. 

The demo application is available in [this repository](https://github.com/openworm/geppetto-application) which you can fork to build your own. Every Geppetto application has an npm dependency on [geppetto-client](https://github.com/openworm/geppetto-client/tree/development) which makes all the frontend Geppetto components and infrastructure available to the application. A Geppetto application can be deployed on different backends based on Java (via Eclipse Virgo) or Python (via [Jupyter Notebook](https://github.com/openworm/org.geppetto.frontend.jupyter) or [Django](https://github.com/MetaCell/pygeppetto-django)).

#### Web client
  The [Geppetto Client](https://github.com/openworm/geppetto-client/tree/development) is reused in all Geppetto applications. It contains all the GUI components, the Javascript facilities to interact with the Geppetto Model and the infrastructure to communicate with the backend. The Geppetto client is available from [npm](https://www.npmjs.com/package/@geppettoengine/geppetto-client).

#### Java backend
The Java backend is the reference backend implementation and is used in client-server deployments of Geppetto. The Java backend is modular allowing each deployment to be customised only with the relevant bundles.
 * Essential
   * [org.geppetto.model](https://github.com/openworm/org.geppetto.model) [![Build Status](https://travis-ci.org/openworm/org.geppetto.model.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.model)
   * [org.geppetto.core](https://github.com/openworm/org.geppetto.core) [![Build Status](https://travis-ci.org/openworm/org.geppetto.core.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.core)
   * [org.geppetto.simulation](https://github.com/openworm/org.geppetto.simulation) [![Build Status](https://travis-ci.org/openworm/org.geppetto.simulation.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.simulation)
   * [org.geppetto.frontend](https://github.com/openworm/org.geppetto.frontend) [![Build Status](https://travis-ci.org/openworm/org.geppetto.frontend.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.frontend) (Note: the repository of the geppetto application you want to deploy in a Java Backend needs to be cloned inside this bundle)
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
      
#### Python Backend (working prototype, in development)

Python backends are being developed both on top of [Django](https://github.com/MetaCell/pygeppetto-django) and as a [Jupyter Notebook extension](https://github.com/openworm/org.geppetto.frontend.jupyter). The Jupyter extension allows the user to host a Geppetto application inside a Jupyter Notebook environment. The application will talk to the Python kernel of the notebook which will act as a backend. Client-server deployments based on the Jupyter Notebook extension are also possible using Jupyter Hub.

   * [org.geppetto.frontend.jupyter](https://github.com/openworm/org.geppetto.frontend.jupyter)

All Python backends will reuse pyGeppetto as the main library. pyGeppetto contains the code to work with a Geppetto model and to implement the REST and Websockets APIs which is independent of the specific server (e.g., Django, Jupyter, etc.). 
   
   * [pyGeppetto](https://github.com/openworm/pygeppetto) 

#### Node.js Backend (proof of concept)
   * [org.geppetto.frontend.nodejs](https://github.com/openworm/org.geppetto.frontend.nodejs) [![Build Status](https://travis-ci.org/openworm/org.geppetto.frontend.nodejs.png?branch=master)](https://travis-ci.org/openworm/org.geppetto.frontend.nodejs)


#### [Website](http://www.geppetto.org/) | [Documentation](http://docs.geppetto.org/) | [Releases](https://github.com/openworm/org.geppetto/releases/)
#### [Contribution guidelines](http://docs.geppetto.org/en/latest/contribute.html#how-to-contribute-code-to-geppetto) | [Development progress](https://waffle.io/openworm/org.geppetto)

Geppetto is released under the [MIT](http://opensource.org/licenses/MIT) license.

<p align="center">
  <img src="http://www.geppetto.org/images/geppetto.png" alt="Geppetto"/>
</p>
