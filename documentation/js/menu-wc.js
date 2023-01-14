'use strict';

customElements.define('compodoc-menu', class extends HTMLElement {
    constructor() {
        super();
        this.isNormalMode = this.getAttribute('mode') === 'normal';
    }

    connectedCallback() {
        this.render(this.isNormalMode);
    }

    render(isNormalMode) {
        let tp = lithtml.html(`
        <nav>
            <ul class="list">
                <li class="title">
                    <a href="index.html" data-type="index-link">dazzle-backend-main documentation</a>
                </li>

                <li class="divider"></li>
                ${ isNormalMode ? `<div id="book-search-input" role="search"><input type="text" placeholder="Type to search"></div>` : '' }
                <li class="chapter">
                    <a data-type="chapter-link" href="index.html"><span class="icon ion-ios-home"></span>Getting started</a>
                    <ul class="links">
                        <li class="link">
                            <a href="overview.html" data-type="chapter-link">
                                <span class="icon ion-ios-keypad"></span>Overview
                            </a>
                        </li>
                        <li class="link">
                            <a href="index.html" data-type="chapter-link">
                                <span class="icon ion-ios-paper"></span>README
                            </a>
                        </li>
                                <li class="link">
                                    <a href="dependencies.html" data-type="chapter-link">
                                        <span class="icon ion-ios-list"></span>Dependencies
                                    </a>
                                </li>
                                <li class="link">
                                    <a href="properties.html" data-type="chapter-link">
                                        <span class="icon ion-ios-apps"></span>Properties
                                    </a>
                                </li>
                    </ul>
                </li>
                    <li class="chapter modules">
                        <a data-type="chapter-link" href="modules.html">
                            <div class="menu-toggler linked" data-toggle="collapse" ${ isNormalMode ?
                                'data-target="#modules-links"' : 'data-target="#xs-modules-links"' }>
                                <span class="icon ion-ios-archive"></span>
                                <span class="link-name">Modules</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                        </a>
                        <ul class="links collapse " ${ isNormalMode ? 'id="modules-links"' : 'id="xs-modules-links"' }>
                            <li class="link">
                                <a href="modules/AppModule.html" data-type="entity-link" >AppModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#controllers-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' : 'data-target="#xs-controllers-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' }>
                                            <span class="icon ion-md-swap"></span>
                                            <span>Controllers</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="controllers-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' :
                                            'id="xs-controllers-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' }>
                                            <li class="link">
                                                <a href="controllers/AppController.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AppController</a>
                                            </li>
                                        </ul>
                                    </li>
                                <li class="chapter inner">
                                    <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                        'data-target="#injectables-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' : 'data-target="#xs-injectables-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' }>
                                        <span class="icon ion-md-arrow-round-down"></span>
                                        <span>Injectables</span>
                                        <span class="icon ion-ios-arrow-down"></span>
                                    </div>
                                    <ul class="links collapse" ${ isNormalMode ? 'id="injectables-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' :
                                        'id="xs-injectables-links-module-AppModule-217db188dabb3c1ecb9f77f058b63e5a00514abc4208cbf2e8f1ac618f7b2171355a4fc25a5adcf987b1c3ee2e94aba2c13b54a72cdc9ea7b7fc12a84aa133fe"' }>
                                        <li class="link">
                                            <a href="injectables/AppService.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AppService</a>
                                        </li>
                                    </ul>
                                </li>
                            </li>
                            <li class="link">
                                <a href="modules/FeaturesModule.html" data-type="entity-link" >FeaturesModule</a>
                                <li class="chapter inner">
                                    <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                        'data-target="#injectables-links-module-FeaturesModule-4f60709db14ab08d0dc09a621fd0f2bfe858960ccf716adc3f72a909156b946139bae88962425a68f8daf15d9a0e1d276d4a96fa3b77374423094c0e66c5f593"' : 'data-target="#xs-injectables-links-module-FeaturesModule-4f60709db14ab08d0dc09a621fd0f2bfe858960ccf716adc3f72a909156b946139bae88962425a68f8daf15d9a0e1d276d4a96fa3b77374423094c0e66c5f593"' }>
                                        <span class="icon ion-md-arrow-round-down"></span>
                                        <span>Injectables</span>
                                        <span class="icon ion-ios-arrow-down"></span>
                                    </div>
                                    <ul class="links collapse" ${ isNormalMode ? 'id="injectables-links-module-FeaturesModule-4f60709db14ab08d0dc09a621fd0f2bfe858960ccf716adc3f72a909156b946139bae88962425a68f8daf15d9a0e1d276d4a96fa3b77374423094c0e66c5f593"' :
                                        'id="xs-injectables-links-module-FeaturesModule-4f60709db14ab08d0dc09a621fd0f2bfe858960ccf716adc3f72a909156b946139bae88962425a68f8daf15d9a0e1d276d4a96fa3b77374423094c0e66c5f593"' }>
                                        <li class="link">
                                            <a href="injectables/FeaturesService.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >FeaturesService</a>
                                        </li>
                                    </ul>
                                </li>
                            </li>
                </ul>
                </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ? 'data-target="#miscellaneous-links"'
                            : 'data-target="#xs-miscellaneous-links"' }>
                            <span class="icon ion-ios-cube"></span>
                            <span>Miscellaneous</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="miscellaneous-links"' : 'id="xs-miscellaneous-links"' }>
                            <li class="link">
                                <a href="miscellaneous/functions.html" data-type="entity-link">Functions</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <a data-type="chapter-link" href="coverage.html"><span class="icon ion-ios-stats"></span>Documentation coverage</a>
                    </li>
                    <li class="divider"></li>
                    <li class="copyright">
                        Documentation generated using <a href="https://compodoc.app/" target="_blank">
                            <img data-src="images/compodoc-vectorise.png" class="img-responsive" data-type="compodoc-logo">
                        </a>
                    </li>
            </ul>
        </nav>
        `);
        this.innerHTML = tp.strings;
    }
});