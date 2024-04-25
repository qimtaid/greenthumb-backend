import React from "react";
import ProductCategoryRow from "./ProductCategoryRow";
import ProductRow from "./ProductRow";

function ProductTable({ products, search, showInStock }) {
  
  const filteredProducts = products
    .filter(product => {
      if (showInStock) {
        return product.stocked
      } else {
        return true
      }
    })
    .filter(product => product.name.includes(search))

  const rows = [];
  let lastCategory;
  for (const product of filteredProducts) {
      if (product.category !== lastCategory) {
          rows.push(<ProductCategoryRow key={product.category} category={product.category} />)
      }
      rows.push(<ProductRow key={product.name} name={product.name} stocked={product.stocked} price={product.price} />)
      lastCategory = product.category
  }

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  )
}

export default ProductTable