
## pertanyaan umum unwaha
* getCollegeInfo
  - utter_getCollegeInfo

## visi+misi unwaha
* getVisiMisiUnwaha
  - utter_getVisiUnwaha
  - utter_getMisiUnwaha

## pertanyaan umum unwaha+ paham
* getCollegeInfo
  - utter_getCollegeInfo
  - utter_clear
* clear
  - utter_paham

## pertanyaan umum unwaha + tidak paham
* getCollegeInfo
  - utter_getCollegeInfo
  - utter_clear
* confuse
  - utter_confuse

## pertanyaan umum unwaha + tidak
* getCollegeInfo
  - utter_getCollegeInfo
  - utter_clear
* deny
  - utter_confuse

## cara daftar
* getRegisterInfo
  - utter_getRegisterInfo

## cara daftar v2
* getRegisterInfo
  - utter_getRegisterInfo
  - utter_getRegisterInfo-2

## cara daftar + step 2
* getRegisterInfo
  - utter_getRegisterInfo
  - getRegisterInfo-step-2

## tanggal test
* test_date
  - utter_test_date

## biaya pendaftaran
* getAdministrationCost
  - utter_getAdministrationCost
  - utter_confuse

## syarat pendaftaran
* register_requirement
  - utter_register_requirement

## biaya kuliah
* getCostInfo
  - utter_getCostInfo

## biaya kuliah v2
* getCostInfo
  - utter_getCostInfo
  - utter_confuse

## tanya alamat
* getCollegeAddressInfo
  - utter_getCollegeAddressInfo

## penjelasan fakultas
* getGeneralFacultyInfo
  - utter_getGeneralFacultyInfo

## penjelasan prodi
* getGeneralMajorInfo
  - utter_getGeneralMajorInfo

## perbedaan prodi dengan fakultas
* getDifferentProdi-Faculty
  - utter_getDifferentProdi-Faculty

## penjelasan fakultas di unwaha
* getFaculty
  - utter_getFaculty

## tampilkan list semua prodi
* getProdiGeneral
  - utter_getProdiGeneral
  - utter_getProdiInFIP
  - utter_getProdiInFAI
  - utter_getProdiInFE
  - utter_getProdiInFP
  - utter_getProdiInFTI

## career 
* getCareer
 - action_career

## career + affirm
* getCareer
 - action_career
* affirm
  - utter_paham