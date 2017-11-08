#include "globalconfig.h"

u8 mystrcmp(u8 *str1, u8 *str2, u8 len)
{
	u8 i = 0;
	for(i = 0; i<len; i++)
	{
		if (str1[i] != str2[i])
			return 1;
	}
	return 0;
}

u16 str2u16(u8 *str, u8 start)
{
	u8 i = 0;
	u16 tmp = 0;
	for(i=0;i<MotorNum;i++)
	{
		tmp = tmp*256+str[start+i];
	}
	return tmp;
}

//u8 read_dir_cmd(u8 *str)
//{
//	u8 i = 0;
//	u8 dir[MotorNum];
//	for (i=1;i<MotorNum+1; i++)
//	{
//		dir[i-1] = str[i];
//	}
//	return *dir;
//}


