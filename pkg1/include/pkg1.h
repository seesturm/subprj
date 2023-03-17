#pragma once


#ifdef _WIN32
  #define PKG1_EXPORT __declspec(dllexport)
#else
  #define PKG1_EXPORT
#endif

PKG1_EXPORT void pkg1();
