#include "dirc.h"

void DIR_GPIO_Configuration(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_1 | GPIO_Pin_2;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
}

void Set_ALL_Dir_GPIO(u8 *dirport, u8 *dir)
{
	u8 i = 0;
	for(i=0; i<MOTORNUM; i++)
	{
		PCout(dirport[i]) = dir[i];
	}
}



