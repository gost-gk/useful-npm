'use strict';
module.exports = ${function_name};

const isNumber = require('is-number');
const isString = require('is-string');
const isUndefined = require('is-undefined');
const isNull = require('is-null');
global.jQuery = require('jquery');
require('jquery-basic-arithmetic-plugin');

function ${function_name}(x) {
    // Check if given object is undefined
    if (isUndefined(x)) {
        return false;
    }
    
    // Check if given object is null
    if (isNull(x)) {
        return false;
    }
    
    // Check if given object is string
    if (isString(x)) {
        return false;
    }
    
    // Check if given object is number
    if (!isNumber(x)) {
        return false;
    }
    
    return jQuery.equals(x, ${value});
}
