import React from "react";

function ProductCategoryRow({ category }) {
  return (
    <tr style={{ fontWeight: "bold" }}>
      <td colSpan="2">{category}</td>
    </tr>
  )
}

export default ProductCategoryRow