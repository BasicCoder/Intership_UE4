## Import Need Resource
## Input
> - Place Excel Files into CSV_Data Folder.
## Parameter
> - CsvFileDir : Source file and destination file in this folder.
> - SrcCsvFileName : Source file name.
> - AccordingFieldName : According to this field to get need resource name.
> ---
> - DstCsvFileName : Destination file name.
> - FillFieldName : Need to fill field name.
> - ResourceDir : Need resource directory.
## Output
> - Result will appear in CSV_Data Folder,  **Destination file name = Source file name + WithIcon**
#### Note:
Because source CSV file **don't have**  special field, So it is hard to process, need special process.

---

## MultiColumn Import Need Resource
## Input
> - Place Excel Files into CSV_Data Folder.
## Parameter
> - CsvFileDir : Source file and destination file in this folder.
> - SrcCsvFileName : Source file name.
> - AccordingFieldNames : It is a list, according to this field to get need resource name.
> ---
> - DstCsvFileName : Destination file name.
> - FillFieldNames : It is a list, need to fill field name.
> - ResourceDirs : Need resource directories.
## Output
> - Result will appear in CSV_Data Folder