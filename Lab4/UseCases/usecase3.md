**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Clear Canvas with Space Key

**Primary Actor**: user

**Goal in Context**: To clear the entire canvas in the drawing application by pressing the space key. This action will replace all pixels with the last selected color, effectively filling the canvas with that color.

**Preconditions**: The graphics program must be running and in a responsive state. The user must have previously selected a color.

**Trigger**: The user presses the space key to clear the canvas.

**Scenario**: 1. The user presses the space key on the keyboard. 2. The application detects the space key press as a request to clear the canvas. 3. The application fills the entire canvas with the last selected color (e.g., red), effectively removing all previously drawn elements and replacing them with the selected color. 4. The canvas is now entirely filled with the last selected color.

**Exceptions**: If the user presses the space key when there is no previously selected color (i.e., they haven't chosen a color before), the application should provide feedback, such as an error message or a reminder to select a color first.

**Priority**: medium

**When available**: first release

**Channel to actor**: The primary actor interacts with the system through keyboard input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: N/A

<hr>

(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
