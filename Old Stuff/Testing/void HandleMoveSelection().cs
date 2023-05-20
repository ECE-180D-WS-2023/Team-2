void HandleMoveSelection()
{
    currentMove = speech.moveSpeech(playerUnit.Pokemon.Name, playerUnit.Pokemon.Moves[currentMove]);

    dialogBox.UpdateMoveSelection(currentMove, playerUnit.Pokemon.Moves[currentMove]); 

    if (currentMove == playerUnit.Pokemon.Moves[currentMove].Name.ToString()) // toLower(), also probably not a string
    {
        dialogBox.EnableMoveSelector(false);
        dialogBox.EnableDialogText(true);
        StartCoroutine(PlayerMove());
    }
    else if (currentMove == "back")
    {
        dialogBox.EnableMoveSelector(false);
        dialogBox.EnableDialogText(true);
        ActionSelection();
    }
}