#ifndef __TIMER_H
#define __TIMER_H

#include "sys.h"

void TIM2_Congfig_Init(u16 psc);
void TIM_GPIO_Config_Init(void);
void TIM_NVIC_Configuration(void);
void TIM_Startup(void);
void TIM_Shutdown(void);
#endif

