"use strict";

require("mocha");
const assert = require("assert");
const ${function_name} = require("./");

describe("${function_name}", function() {
    it("should return true if the number is ${value}", function() {
        assert(${function_name}(${value}));
    });
  
    it("should return false if the number is not ${value}", function() {
        assert(!${function_name}(${value} + 1));
    });
    
    it("should return false if the number is not a number at all", function() {
        assert(!${function_name}(null));
        assert(!${function_name}(undefined));
        assert(!${function_name}("${value}"));
        assert(!${function_name}({prop: "${value}"}));
    });
});
