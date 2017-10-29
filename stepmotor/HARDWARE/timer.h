#ifndef __TIMER_H
#define __TIMER_H
#include "sys.h"

#define DIR_1A PAout(0)
#define PUL_1A PAout(1)
void TIM2_Int_Init(u16 arr, u16 psc);
#endif
