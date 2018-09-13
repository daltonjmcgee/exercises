#include <stdio.h>

int main(){
  int guests;
  printf("How many guests does Pupeta have? ");
  scanf("%d", &guests);
  if (guests == 0)
    printf("Pupeta's Mood: Sad and will force you to listen to his story, will make you late.\n" );
  else if (guests == 1)
    printf("Pupeta's Mood: He will ask you to deliver half of the pizza to his only neighbor, you may be late.\n");
  else if (guests >=2 && guests <= 5)
    printf("Pupeta's Mood: Will have great mood and will be singing song. May crack joke as well. You will get good tips, definitely.\n");
  else if (guests == 6 || guests == 8)
    printf("Pupeta's Mood: Too angry and furious, deliver the pizza and leave ASAP.\n");
  else if (guests == 7)
  printf("Pupeta's Mood: He will be making great drink for his neighbors and will invite you to taste. But will not give you tip.\n");
  else printf("Invalid number of neighbours\n");

return 0;
}
