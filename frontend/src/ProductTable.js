import React, { Component } from 'react';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

function onSelectRow(row, isSelected, e) {
}

const selectRow = {
  mode: 'checkbox',
  clickToSelect: true,
  onSelect: onSelectRow,
  hideSelectColumn: true,  // enable hide selection column.
  bgColor: 'rgb(238, 193, 213)'
};

// Formatting functions
function filterType(cell, row) {
  // just return type for filtering or searching.
  return cell.type;
}

class ProductTable extends Component {
  render() {
    return (
      <div>
        <BootstrapTable exportCSV data={this.props.data}
        selectRow={selectRow}
        search = {true}
        variant = "dark"
        pagination
        tableStyle={ { border: '#0000FF 2.5px solid' } }
        containerStyle={ { border: 'black 2.5px solid' } }
        bodyStyle={ { border: 'green 1px solid' } }
        >
          <TableHeaderColumn isKey dataField='prdct_id' dataSort> Product ID </TableHeaderColumn>
          <TableHeaderColumn dataField='name' dataSort> Variety Name </TableHeaderColumn>
          <TableHeaderColumn dataField='skin_color' dataSort> Colour of Skin </TableHeaderColumn>
          <TableHeaderColumn dataField='maturity' dataSort>Maturity</TableHeaderColumn>
          <TableHeaderColumn dataField='country' dataSort>Country</TableHeaderColumn>
          <TableHeaderColumn dataField='height' dataSort>Height of Plants</TableHeaderColumn>
        </BootstrapTable>
      </div>
    );
  }
}
export default ProductTable;
