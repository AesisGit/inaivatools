from django.shortcuts import render
from .forms import compare_lists_input_form


# Create your views here.
def compare_lists(request):
    
    
    if request.method == 'POST':
        listsToCompare = compare_lists_input_form(request.POST)
        if listsToCompare.is_valid():

            inputList1 = listsToCompare['inputText1'].value()
            inputList2 = listsToCompare['inputText2'].value()
            listDifferences = ""

##            mergeBy = listsToCompare['joinBy'].value()
            
            #replacing \r\n with a "," character and then create lists from inputLists strings
            inputList1 = inputList1.replace("\r\n", ",")
            inputList2 = inputList2.replace("\r\n", ",")
            inputList1 = list(inputList1.split(","))
            inputList2 = list(inputList2.split(","))
            
            #Process the lists and get the result
             
            
            #Display the result data
            data = {'inputText1': inputList1, 'inputText2': inputList2, 'listDifferences': listDifferences}
            listsToCompare = compare_lists_input_form(initial=data)
            
            return render(request, 'compareLists/comparelists.html', {'listsToCompare': listsToCompare})

    else:
        listsToCompare = compare_lists_input_form()
        return render(request, 'compareLists/comparelists.html', {'listsToCompare': listsToCompare})