import React from 'react';
import ReactDOM from 'react-dom';
import FilterableProductTable from "../src/components/FilterableProductTable"
import { products } from "../src/components/data"

/*
Thinking in React: https://reactjs.org/docs/thinking-in-react.html

Step 1: Break The UI Into A Component Hierarchy

  FilterableProductTable
  ├───SearchBar
  └───ProductTable
      ├───ProductCategoryRow
      └───ProductRow

Step 2: Build A Static Version in React


Step 3: Identify The Minimal (but complete) Representation Of UI State

- The original list of products (don't need state! - props)
- The search text the user has entered (state)
- The value of the checkbox (state)
- The filtered list of products (don't need state! - computed from props + state)

- Is it passed in from a parent via props? If so, it probably isn’t state.
- Does it remain unchanged over time? If so, it probably isn’t state.
- Can you compute it based on any other state or props in your component? If so, it isn’t state.

filteredProduct = products.filter(product => product.name === search)

Step 4: Identify Where Your State Should Live

- Identify every component that renders something based on that state. 
  - (SearchBar and ProductTable)
- Find a common owner component (a single component above all the components that need the state in the hierarchy).
  - (FilterableProductTable)
- Either the common owner or another component higher up in the hierarchy should own the state.
- If you can’t find a component where it makes sense to own the state, create a new component solely for holding the state and add it somewhere in the hierarchy above the common owner component.

Step 5: Add Inverse Data Flow


*/

ReactDOM.render(<FilterableProductTable products={products} />, document.getElementById('root'));