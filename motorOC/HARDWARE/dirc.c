#include "dirc.h"
#include "globalconfig.h"

GPIO_TypeDef *Dir_GPIO_Port[MotorNum] = {GPIOC, GPIOC, GPIOC, GPIOC};
u16 Dir_Pins[MotorNum] = {GPIO_Pin_1, GPIO_Pin_2, GPIO_Pin_3, GPIO_Pin_4};
u16 Dir_Pins_Connect = GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3 | GPIO_Pin_4;

void DIR_GPIO_Configuration(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = Dir_Pins_Connect;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
}

void Set_ALL_Dir_GPIO(u8 *dir)
{
	u8 i = 0;
	for(i=0; i<MotorNum; i++)
	{
		if(dir[i]==1)
		{
			GPIO_SetBits(Dir_GPIO_Port[i], Dir_Pins[i]);
		}
		else
		{
			GPIO_ResetBits(Dir_GPIO_Port[i], Dir_Pins[i]);
		}
	}
}



