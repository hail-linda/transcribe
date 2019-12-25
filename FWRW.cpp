
#define MAXPATH 800
#include <iostream>
#include <Windows.h>
#include <direct.h>
#include <string.h>
#include <stdio.h>
using namespace std;

int main(int argc, char* argv[])
{
	char buffer[MAXPATH];
	LPWSTR buf[1000];
	TCHAR exeFile[1000];
	GetModuleFileName(NULL, exeFile, MAXPATH);
	lstrcat(exeFile, L"\\..\\wallpaper.jpg");
	//wcout << exeFile << endl;
	const wchar_t* filenm = L"123.bmp";
	if (SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, exeFile, SPIF_SENDCHANGE))
	{
		
		//cout << "succeed!!" << endl;
		//cout << strcat_s(buffer, filenm) << endl;

	}
	else
		cout << "fail!!" << endl;
}

