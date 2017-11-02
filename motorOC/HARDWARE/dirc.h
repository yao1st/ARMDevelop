#ifndef __DIRC_H
#define __DIRC_H

#include "sys.h"

#define MOTORNUM 2
void DIR_GPIO_Configuration(void);
void Set_ALL_Dir_GPIO(u8 *dirport, u8 *dir);

#endif


