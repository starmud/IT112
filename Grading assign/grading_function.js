// function calculates grade, prints pop up message

function assignedScore(score) {
    if (score >= 90) {
        return "Wow, You scored an A!";
      } 
      else if (score >= 80) {
        return "You scored a B!";
      } 
      else if (score >= 70) {
        return "You scored a C!";
      } 
      else if (score >= 60) {
        return "You scored a D!";
      } 
      else {
        return "You scored an F!";
      }
    }