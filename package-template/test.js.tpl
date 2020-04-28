"use strict";

require("mocha");
const assert = require("assert");
const ${module_name} = require("../");

describe("${module_name}", function() {
    it("should return true if the number is ${value}", function() {
        assert(${function_name}(${value}));
    });
  
    it("should return false if the number either is not ${value} or is not a number at all", function() {
        assert(!${function_name}(${value} + 1));
        assert(!${function_name}(null));
        assert(!${function_name}(undefined));
        assert(!${function_name}("${value}"));
    });
});
