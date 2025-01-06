Const listlength As Integer = 10
Dim listitem(listlength) As String
listitem = {"I", "H", "G", "F", "E", "D", "C", "B", "A", "J"}
Console.Write("Enter the item to find: ")
Dim searchedFor As String = Console.ReadLine

'Linear search algoirithm
Dim found As Boolean = False
Dim position As Integer = 0
While found = False And position <= listlength - 1
	If listitem(position) = searchedFor Then
		found = True
            Else
                position += 1
            End If
End While

'Output item or error
If found = True Then
	Console.WriteLine("Item found at " & position)
Else
	Console.WriteLine("Item not found in list")
End If