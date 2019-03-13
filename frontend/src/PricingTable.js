import React, { Component } from 'react';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

function onSelectRow(row, isSelected, e) {
}

const selectRow = {
  mode: 'checkbox',
  clickToSelect: true,
  //unselectable: [2], // give rowkeys
  onSelect: onSelectRow,
  hideSelectColumn: true,  // enable hide selection column.
  bgColor: 'rgb(238, 193, 213)'
};

const cellEditProp = {
  mode: 'dbclick', //Double click to edit cell
};

// Formatting functions
function formatFloat(cell, row) {
  return parseFloat(cell);
}

function dateFormatter(cell, row) {
  return `${('0' + cell.getDate()).slice(-2)}/${('0' + (cell.getMonth() + 1)).slice(-2)}/${cell.getFullYear()}`;
}

function filterType(cell, row) {
  // just return type for filtering or searching.
  return cell.type;
}

const options = {
  insertText: 'Add Price',
  deleteText: 'Remove Price',
  exportCSVText: 'export csv',
  saveText: 'my_save',
  closeText: 'my_close',

  //onRowClick: function(row) {
    //alert(`You click row id: ${row.id}`);
  //},
  //onRowDoubleClick: function(row) {
    //alert(`You double click row id: ${row.id}`);
  //}
};


class PricingTable extends Component {
  render() {
    return (
      <div>
        <BootstrapTable insertRow deleteRow exportCSV data={this.props.data}
        selectRow={selectRow}
        cellEdit={cellEditProp}
        options={options}
        search = {true}
        variant = "dark"
        pagination
        tableStyle={ { border: '#0000FF 2.5px solid' } }
        containerStyle={ { border: 'black 2.5px solid' } }
        bodyStyle={ { border: 'green 1px solid' } }
        >
          <TableHeaderColumn isKey dataField='date' dataSort> Date </TableHeaderColumn>
          <TableHeaderColumn dataField='client_id' dataSort> Cient ID </TableHeaderColumn>
          <TableHeaderColumn dataField='prdct_id' dataSort> Product id </TableHeaderColumn>
          <TableHeaderColumn dataField='price' dataFormat={ formatFloat } filterValue={filterType} dataSort>
            Price
          </TableHeaderColumn>
          <TableHeaderColumn dataField='quantity' dataSort>Quantity</TableHeaderColumn>
          <TableHeaderColumn dataField='validated' dataSort>Validated</TableHeaderColumn>
        </BootstrapTable>
      </div>
    );
  }
}
export default PricingTable;
