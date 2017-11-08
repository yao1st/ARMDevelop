#ifndef __LED_H
#define __LED_H	 
#include "sys.h"

#define LED0 PBout(5)// PB5
#define LED1 PEout(5)// PE5	

void LED_Init(void);//≥ı ºªØ
void LED1_Flicker(u16 times);
void LED0_Flicker(u16 times);
		 				    
#endif
