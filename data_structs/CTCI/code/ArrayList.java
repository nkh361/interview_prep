ArrayList<String> merge(String[] words, String[] more){
  ArrayList<String> sentence = new ArrayList<string>();
  for (String w : words) sentence.add(w);
  for (String w : more) sentence.add(w);
  return sentence;
}
