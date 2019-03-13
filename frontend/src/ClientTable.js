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
  blurToSave: true
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


class ClientTable extends Component {
  render() {
    return (
      <div>
        <BootstrapTable exportCSV data={this.props.data}
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
          <TableHeaderColumn isKey dataField='client_id' dataSort> Cient ID </TableHeaderColumn>
          <TableHeaderColumn dataField='first_name' dataSort> First Name </TableHeaderColumn>
          <TableHeaderColumn dataField='last_name' dataSort> Last Name </TableHeaderColumn>
          <TableHeaderColumn dataField='type' dataSort>Client Type</TableHeaderColumn>
          <TableHeaderColumn dataField='location' dataSort>Location</TableHeaderColumn>
        </BootstrapTable>
      </div>
    );
  }
}
export default ClientTable;
