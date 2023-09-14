export default function appendToEachArrayValue(array, appendString) {
  const xarray = [];
  for (const idx of array) {
    const value = array[idx];
    xarray[idx] = appendString + value;
  }

  return xarray;
}
