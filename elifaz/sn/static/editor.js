dojo.require("dijit.Editor");

// extra plugins
dojo.require("dijit._editor.plugins.FontChoice");
dojo.require("dijit._editor.plugins.FullScreen");
dojo.require("dijit._editor.plugins.LinkDialog");
dojo.require("dijit._editor.plugins.ViewSource");
dojo.require("dojox.editor.plugins.Blockquote");
dojo.require("dojox.editor.plugins.FindReplace");
dojo.require("dojox.editor.plugins.InsertAnchor");
dojo.require("dojox.editor.plugins.InsertEntity");
dojo.require("dojox.editor.plugins.PasteFromWord");
dojo.require("dojox.editor.plugins.ShowBlockNodes");
dojo.require("dojox.editor.plugins.TextColor");

// headless plugins
dojo.require("dojox.editor.plugins.AutoUrlLink");
dojo.require("dojox.editor.plugins.NormalizeIndentOutdent");
//dojo.require("dojox.editor.plugins.PrettyPrint"); // let's pretty-print our HTML
dojo.require("dojox.editor.plugins.ToolbarLineBreak");

dojo.ready(function(){
  var textareas = dojo.query("textarea");
  if(textareas && textareas.length){
    dojo.addClass(dojo.body(), "claro");
    dojo.forEach(textareas, function(textarea) {
            
        //Create the editor on click
    	dojo.connect(textarea, 'click', function (event) {
    	
    		dojo.style(textarea, {'display' : 'none'});
    			
    	    var editor_div = dojo.create('div');
    	    dojo.place(editor_div, textarea, 'after');
    	 	dojo.style(editor_div, {
    	 	 				 height	: '340px',
    	 	 				 width  : '610px',
    	 					 'float'	: 'left',});
    	 	
    	 
    	 					 
       		var editor = new dijit.Editor({
		      plugins: [
			  "fullscreen", "showblocknodes", "viewsource", "|",
			  "undo", "redo", "|",
			  "cut", "copy", "paste", "pastefromword", "|",
			  "findreplace", "||",
		          "formatBlock", "blockquote", "insertOrderedList", "insertUnorderedList", "|",  
		          "bold", "italic", "underline", "strikethrough", "|",
			  "createLink", "insertanchor", "insertEntity", "insertImage",
		          // headless plugins
		          "normalizeindentoutdent",
			  // "prettyprint",
		          "autourllink", "dijit._editor.plugins.EnterKeyHandling"
		      ],
		      onBlur: function (event) {
		      	textarea.value = this.get('value');
		      	//Destroy the editor on blur
		      	editor_div.parentNode.removeChild(editor_div);
		      	dojo.style(textarea, {'display' : 'block'});
		      	this.destroyRecursive();
		      }
		    }, editor_div);
		    
			editor.onLoadDeferred.then(function () {
				editor.set('value', textarea.value);
				editor.focus();
			})
    	});
    });
  }
});
