/** @odoo-module **/

import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { browser } from "@web/core/browser/browser";
import { symmetricalDifference } from "@web/core/utils/arrays";
import { _t, qweb as QWeb } from "web.core";


const { Component, useState } = owl;
const session = require("web.session");
const rpc = require("web.rpc");
var show_company = false;
session.user_has_group("base.group_multi_company").then(function (has_group) {
  show_company = has_group;
});
var start_search_after_letter = 0

	

export class GlobalSearch extends Component {
    setup() {
       	var self = this;
        this._search_def = $.Deferred();
        this.show_company = show_company;
        this.allowed_company_ids = String(session.user_context.allowed_company_ids)
        .split(",")
        .map(function (id) {
            return parseInt(id);
        });
        this.current_company = this.allowed_company_ids[0];
        rpc.query({	
	    	model: "res.company",
	    	method: "search_read",
	    	args: [[["id", "=", self.current_company]], ["start_search_after_letter"]],
    	}).then(function (data) {
    		if(data){
    			if(data && data[0]){
    				start_search_after_letter = data[0].start_search_after_letter;
    			}
    			
    		}
    		
    	});

	    	
    }
    onSearchResultsNavigate(){
    	this._search_def.reject();
	      this._search_def = $.Deferred();
	      setTimeout(this._search_def.resolve.bind(this._search_def), 500);
	      
	      this._search_def.done(this._searchData.bind(this));
	       
	      return;
    }
    _on_click_clear_Search(){
    	$(".sh_search_input input").val('');
        $(".sh_search_results").empty();
    }
  
    _searchData() {
    	
      var query = $(".sh_search_input input").val();
      if (query === "") {
        $(".sh_search_container").removeClass("has-results");
        $(".sh_search_results").empty();
        return;
      }
      $(".sh_search_results").empty();
      var self = this;
      if (query.length >=start_search_after_letter) {
          rpc.query({
              model: "global.search",
              method: "get_search_result",
              args: [[query]],
          }).then(function (data) {
              if (data) {
                  self._searchableMenus = data;

                  // var results = fuzzy.filter(query, _.keys(self._searchableMenus), {});

                  var results = _.keys(self._searchableMenus);
                  $(".sh_search_results").toggleClass("has-results", Boolean(results.length));
                  
                  $(QWeb.render('MenuSearchResults', {
                	  results: results,
                	  widget:self,
                	  _checkIsMenu: (key) => {
                          console.log('123',key)
                           key = key.split("|")[0];
					      if (key == "menu") {
					          return true;
					      } else {
					          return false;
					      }
                        },
                        _linkInfo: (key) => {
                        	var original = self._searchableMenus[key];
                        	return original;
                         },
                         _getFieldInfo: (key) => {
                        	 key = key.split("|")[1];
                        	 return key;
                          },
                          _getcompanyInfo: (key) => {
                        	  key = key.split("|")[0];
                            return key;
                           },
                           _linkInfo: (key) => {
                           	var original = self._searchableMenus[key];
                           	return original;
                            }
                         
                        
                  })).appendTo($(".sh_search_results"));
                  
                  
                
              }
          });
      }
  }
  
}
GlobalSearch.template = "GlobalSearch";
GlobalSearch.components = { Dropdown, DropdownItem };
GlobalSearch.toggleDelay = 1000;

export const systrayItem = {
    Component: GlobalSearch,
};

registry.category("systray").add("GlobalSearch", systrayItem, { sequence: 1 });



