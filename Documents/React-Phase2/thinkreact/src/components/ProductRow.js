import React from "react";

function ProductRow({ price, stocked, name }) {
  const style = stocked ? null : { color: "red", fontWeight: "bold" }
  return (
    <tr>
      <td style={style}>{name}</td>
      <td>{price}</td>
    </tr>
  )
}

export default ProductRow