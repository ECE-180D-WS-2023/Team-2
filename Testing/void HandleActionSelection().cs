void HandleActionSelection()
{
    currentAction = speech.menuSpeech();

    dialogBox.UpdateActionSelection(currentAction);

    if(currentAction == "fight")
    {
        //Fight
        MoveSelection();
    }
    else if(currentAction == "bag")
    {
        //Bag
    }
    else if (currentAction == 2)
    {
        //Pokemon
        OpenPartyScreen();
    }
    else if (currentAction == 3)
    {
        //Run
    }
}