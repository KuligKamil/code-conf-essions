

# DOM Document Object Model

* Programming interface for HTML and XML documents
* Represents the structure of a document as a tree of nodes
* Can be manipulated with JavaScript to change the structure, style, and content of a webpage

# VDOM Virtual Document Object Model

* Virtual representation of the actual DOM (e.g. with JavaScript objects)

* In the memory, not in the browser

* Synced with the real DOM

* What Vue or React uses under the hood

## Why do we need VDOM?

* Decoupling the rendering logic from the real DOM 
* Easier to programmatically manipulate & inspect
* Easier to reuse outside of the browser (e.g. native mobile.server-side rendering, testing) 

<!-- # BOM Browser Object Model -->

